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
      <el-menu-item index="4" disabled>
        <el-tag type="info" style="backgroundColor: black; color: white">Rinkeby Support</el-tag>
      </el-menu-item>   
    </el-menu>
    <h2 style="margin: 20px 0">音声登録</h2>
    <el-card class="box-card" style="margin: 20px 0">
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="タイトル">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="音声">
          <input type="file" :multiple="false" accept="mp3/*" @change="detectFiles($event)">
        </el-form-item>
        <el-form-item label="発行量">
          <el-input-number v-model="form.supply" @change="handleChange" :min="1"></el-input-number>
        </el-form-item>
        <el-form-item label="金額">
          <el-input-number v-model="form.price" @change="handleChange"></el-input-number>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">発行</el-button>
          <el-button>リセット</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <div>
      <h3 style="margin: 10px 0">トランザクション</h3>
      <el-card class="box-card">
        <div class="text item">{{transaction}}</div>
      </el-card>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import Web3 from 'web3'
import abi from '../plugins/abi'
import axios from "axios"
var web3

// init client web3 js
if (process.browser) {
  console.log('givenProvider=')
  console.log(Web3.givenProvider)
  web3 = new Web3(Web3.givenProvider)
}

// const contract = new web3.eth.Contract(abi, '0xfd55cdf84a5545971341f17e4746cd300301aee3')
const contract = new web3.eth.Contract(abi, process.env.contract_addr)
export default {
  components: {
    Logo
  },
  data() {
    return {
      address: '',
      form: {
        name: '',
        supply: 1,
        price: 1000000000,
        voice: ''
      },
      transaction: ''
    };
  },
  async asyncData() {
    const addresses = await web3.eth.getAccounts()
    const address = addresses[0]
    console.log(address)
    return {address: address}
  },
  async created() {
    const address = await web3.eth.defaultAccount
    contract.methods.name().call()
    .then((result) => {
      console.log(result)
    })
  },
  methods: {
    handleChange(value) {
      console.log(value)
    },
    async onSubmit() {
      // console.log(this.$refs)
      const response = await axios.get(`idol_token/register_item/?title=${this.form.name}&address=${this.address}`, {
        baseURL: 'https://idol-token-web.herokuapp.com/',
        headers: { "Content-Type": "application/json", 'X-Requested-With': 'XMLHttpRequest' },
        responseType: 'json',
        data: {}
      })
      console.log(response.data.id)
      // const BN = web3.utils.BN;
      // const numString = new BN(this.form.price).toString();
      contract.methods.releaseVoice(
        response.data.id,
        this.form.supply,
        this.form.price
      )
      .send({
          from: this.address,
          gas: 3000000,
          gasPrice: '3000000'
      })
      .on('transactionHash', (hash) => {
        this.transaction = hash
      })
      .on('confirmation', (confirmationNumber, receipt) => {
        if(receipt.status) {
          this.$router.push({ path: `/idol/${receipt.from}` })
        }
      })
    },
    detectFiles(e) {
      // アップロード対象は1件のみとする
      const file = (e.target.files || e.dataTransfer.files)[0]
      this.form.voice = file
    }
  }
}
</script>