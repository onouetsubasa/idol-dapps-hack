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
    <h2 style="margin: 20px 0">おすすめ</h2>
    <div class="recomend">
      <el-row justify="center" >
        <el-col class="card" :span="4"  v-for="i in idols.recomends" :key="i.id">
          <a :href="`/idol/${i.address}`">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="i.image" class="image">
            <div style="padding: 14px;">
              <span>{{ i.name }}</span>
            </div>
          </el-card>
          </a>
        </el-col>
      </el-row>
    </div>
    <h2 style="margin: 20px 0">ランキング</h2>
    <div class="ranking">
      <el-row justify="center" >
        <el-col class="card" :span="4"  v-for="i in idols.ranking" :key="i.id">
          <a :href="`/idol/${i.address}`">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="i.image" class="image">
            <div style="padding: 14px;">
              <span>{{ i.name }}</span>
            </div>
          </el-card>
          </a>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import abi from '~/plugins/abi'
import Web3 from 'web3'
// import jsonIdol from '~/assets/idol.json'
import axios from "axios"
var web3

// init client web3 js
if (process.browser) {
  web3 = new Web3(Web3.givenProvider)
}

export default {
  components: {
    Logo
  },
  data() {
    return {
      idols: {
        recomends: [],
        ranking: []
      }
    }
  },
  async asyncData({ app }) {
    const response = await axios.get('idol_token/index/', {
      baseURL: 'https://idol-token-web.herokuapp.com',
      headers: { "Content-Type": "application/json", 'X-Requested-With': 'XMLHttpRequest' },
      responseType: 'json',
      data: {}
    })
    console.log(response.data)
    return { idols: response.data}

    // web3.eth.getAccounts(console.log);
    // const contract = new web3.eth.Contract(abi, '0x2b5af53e4d1277271c440d0b7209bf50b8d42b94')
    // contract.methods.name().call()
    // .then((result) => {
    //   console.log(result)
    // })

  }
}
</script>

<style>
  .time {
    font-size: 13px;
    color: #999;
  }

  .card {
    margin: 10px
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>
