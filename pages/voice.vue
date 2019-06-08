<template>
  <div class="container">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">Top</el-menu-item>
      <el-menu-item index="2">
        <nuxt-link to="/voice">商品登録</nuxt-link>
      </el-menu-item>
    </el-menu>
    <h3>商品登録</h3>
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="タイトル">
        <el-input v-model="form.name"></el-input>
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
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import Web3 from 'web3'
import abi from '../plugins/abi'
var web3

// init client web3 js
if (process.browser) {
  console.log('givenProvider=')
  console.log(Web3.givenProvider)
  web3 = new Web3(Web3.givenProvider)
}

const contract = new web3.eth.Contract(abi, '0x2b5af53e4d1277271c440d0b7209bf50b8d42b94')

export default {
  components: {
    Logo
  },
  data() {
    return {
      address: '',
      form: {
        name: '',
        supply: 0,
        price: 0
      }
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
    onSubmit() {
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
    }
  }
}
</script>