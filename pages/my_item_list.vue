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
  <h2 style="margin: 20px 0">マイページ</h2>
  <el-card class="box-card" style="margin: 20px 0">
    <div class="text item" center>
      ADDRESS :  {{ address }}
    </div>
  </el-card>
  <el-card class="box-card" style="margin: 20px 0">
    <el-table
      :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
      style="width: 100%">
      <el-table-column
        label="名前"
        prop="name">
      </el-table-column>
      <el-table-column
        label="総発行量"
        prop="totalSupply">
      </el-table-column>
      <el-table-column
        label="金額"
        prop="price">
      </el-table-column>
      <el-table-column
        align="right">
        <audio :src="require('@/assets/music.mp3')" controls></audio>
      </el-table-column>
    </el-table>
  </el-card>
</div>
</template>

<script>
import Web3 from 'web3'
import abi from '../plugins/abi'
import axios from "axios"
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
        address: '',
        tableData: [],
        search: '',
      }
    },
    async asyncData() {
      const addresses = await web3.eth.getAccounts()
      const address = addresses[0]
      return { address: address }
    },
    created() {
      contract.methods.balanceOf(
        this.address
      ).call()
      .then((result) => {
        const num = web3.utils.hexToNumber(result)
        for(var i=0; i < num; i++) {
          contract.methods.tokenOfOwnerByIndex(
            this.address,
            i
          ).call()
          .then((result) => {
            const tokenId = web3.utils.hexToNumber(result)
            contract.methods.voiceIds(
              tokenId
            ).call()
            .then((result) => {
              const voiceId = web3.utils.hexToNumber(result)
              contract.methods.voices(
                voiceId
              ).call()
              .then(async (result) => {
                console.log("test")
                const response = await axios.get(`idol_token/item/${voiceId}/`, {
                  baseURL: 'https://idol-token-web.herokuapp.com/',
                  headers: { "Content-Type": "application/json", 'X-Requested-With': 'XMLHttpRequest' },
                  responseType: 'json',
                  data: {}
                })
                const totalSupply = web3.utils.hexToNumber(result.totalSupply)
                const issuedNum = web3.utils.hexToNumber(result.issuedNum)
                const price = web3.utils.hexToNumber(result.price)
                console.log({
                  totalSupply: totalSupply,
                  issuedNum: issuedNum,
                  price: price
                })
                this.tableData.push({
                  name: response.data.title,
                  totalSupply: totalSupply,
                  issuedNum: issuedNum,
                  price: price,
                  voiceId: voiceId
                })
              })
            })
          })
        }
      })
    },
    methods: {
      onPlay() {
        var context = new AudioContext();
        var buffer = null;
        var source = context.createBufferSource();

        var request = new XMLHttpRequest();
        request.open('GET', '/Users/takasetoshiaki/Desktop/music.mp3', true);
        request.responseType = 'arraybuffer';
        request.send();

        request.onload = function () {
          var res = request.response;
          console.log("test")
          context.decodeAudioData(res, function (buf) {
            console.log("test")
            source.buffer = buf;
            source.connect(context.destination);
        source.start(0);
          });
        };

        // source.connect(context.destination);
        // source.start(0);
        // new Audio('/Users/takasetoshiaki/Desktop/music.mp3').play();
      },
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    },
  }
</script>