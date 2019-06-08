<template>
<div class="container">
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      label="名前"
      prop="">
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
      align="right">
      <template slot-scope="scope">
        <el-button type="primary" @click="onSubmit">発行</el-button>
        <el-button type="primary" icon="el-icon-lollipop">購入</el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>

<script>
import Web3 from 'web3'
import abi from '~/plugins/abi'

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
        tableData: []
      }
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
              console.log({
                totalSupply: totalSupply,
                issuedNum: issuedNum,
                price: price
              })
              this.tableData.push({
                totalSupply: totalSupply,
                issuedNum: issuedNum,
                price: price
              })
            })
          })
        }
      })
    },
  methods: {
    handleChange(value) {
      console.log(value)
    },
    onSubmit() {
    //   contract.methods.mintvoice(
    //     1
    //   )

      contract.methods.releaseVoice(
        9999,
        this.form.supply,
        this.form.price
      )
      .send({
          from: this.address,
          gas: 30000000,
          gasPrice: '3000000'
      }, (error, transactionHash) => {
        console.log(transactionHash)
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