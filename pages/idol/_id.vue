<template>
<div class="container">
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1">
      <nuxt-link to="/">Top</nuxt-link>
    </el-menu-item>
    <el-menu-item index="2">
      <nuxt-link to="/my_item_list">MyPage</nuxt-link>
    </el-menu-item>
    <el-submenu index="3">
      <template slot="title">アイドルはこちら</template>
        <el-menu-item index="2-1">
          <nuxt-link to="/idol-account">アイドルアカウント登録</nuxt-link>
        </el-menu-item>
        <el-menu-item index="2-2">
          <nuxt-link to="/voice">音声登録</nuxt-link>
        </el-menu-item>
    </el-submenu>    
  </el-menu>
  <el-card class="box-card" style="margin: 20px 0">
    <div class="text item" center>
      ADDRESS :  {{ address }}
    </div>
  </el-card>
  <el-card class="box-card" style="margin: 20px 0">
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        label="名前"
        prop="name">
      </el-table-column>
      <el-table-column
        label="最大発行量"
        prop="totalSupply">
      </el-table-column>
      <el-table-column
        label="発行済み"
        prop="issuedNum">
      </el-table-column>
      <el-table-column
        label="金額"
        prop="price">
      </el-table-column>
      <el-table-column
        label="ID"
        prop="voiceId">
      </el-table-column>
      <el-table-column
        align="right">
        <template slot-scope="scope">
          <el-button type="primary" icon="el-icon-lollipop" value="" @click.native.prevent="onSubmit(scope.$index)">購入</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-card>
</div>
</template>

<script>
import Web3 from 'web3'
import abi from '~/plugins/abi'
import voiceVue from '../voice.vue';
var web3

// init client web3 js
if (process.browser) {
  console.log('givenProvider=')
  console.log(Web3.givenProvider)
  web3 = new Web3(Web3.givenProvider)
}

// const contract = new web3.eth.Contract(abi, '0xe228f3388ac5aaf4a81f9af358ac5dae6bb13028')
let a = process.env.contract_addr
const contract = new web3.eth.Contract(abi, process.env.contract_addr)

  export default {
    data() {
      return {
        address: '',
        tableData: []
      }
    },
    async asyncData() {
      const addresses = await web3.eth.getAccounts()
      const address = addresses[0]
      return { address: address }
    },
    async created() {
      contract.methods.balanceOfOwnedVoices(
        this.$route.params.id
      ).call()
      .then((result) => {
        const num = web3.utils.hexToNumber(result)
        for(var i=0; i < num; i++) {
          contract.methods.ownedVoices(
            this.$route.params.id,
            i
          ).call()
          .then((result) => {
            const voiceId = web3.utils.hexToNumber(result)
            contract.methods.voices(
              voiceId
            ).call()
            .then((result) => {
              const totalSupply = web3.utils.hexToNumber(result.totalSupply)
              const issuedNum = web3.utils.hexToNumber(result.issuedNum)
              const price = web3.utils.hexToNumber(result.price)
              this.tableData.push({
                name: "音声のタイトル",
                totalSupply: totalSupply,
                issuedNum: issuedNum,
                price: price,
                voiceId: voiceId
              })
            })
          })
        }
      })
    },
  methods: {
    handleChange(event) {
      console.log(event)
    },
    onSubmit(index) {
      const voiceId = this.tableData[index].voiceId
      const price = this.tableData[index].price
      console.log(voiceId)
      contract.methods.mintVoice(
        voiceId
      )
      .send({
          from: this.address,
          gas: 3000000,
          gasPrice: web3.eth.gasPrice,
          gasLimit: web3.eth.getBlock("latest").gasLimit,
          value: price
      })
      .on('transactionHash', (hash) => {
        this.transaction = hash
      })
      .on('confirmation', (confirmationNumber, receipt) => {
        if(receipt.status) {
          this.$router.push({ path: `/idol/${receipt.from}` })
        }
      })
    }
  }
  }
</script>