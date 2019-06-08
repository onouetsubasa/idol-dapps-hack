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
    <el-card class="box-card">
      <div class="text item" center>
        ADDRESS :  {{ address }}
      </div>
    </el-card>
  </div>
</template>

<script>
import Web3 from 'web3'
import abi from '../plugins/abi'
var web3

if (process.browser) {
  console.log('givenProvider=')
  console.log(Web3.givenProvider)
  web3 = new Web3(Web3.givenProvider)
}

const contract = new web3.eth.Contract(abi, process.env.contract_addr)
export default {
  data() {
    return {
      address: ''
    };
  },
  async asyncData() {
    const addresses = await web3.eth.getAccounts()
    const address = addresses[0]
    return { address: address }
  },
  async created() {
  },
  methods: {
  }
}
</script>