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
    <h2 style="margin: 20px 0">アイドル登録</h2>
    <el-card class="box-card" style="margin: 20px 0">
      <div class="text item" center>
        ADDRESS :  {{ address }}
      </div>
    </el-card>
    <el-card class="box-card">
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="名前">
          <el-input v-model="name"></el-input>
        </el-form-item>
        <el-form-item label="アイコン">
          <el-upload
            class="avatar-uploader"
            action="https://jsonplaceholder.typicode.com/posts/"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">登録</el-button>
        </el-form-item>
      </el-form>
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
      name: '',
      image: '',
      imageUrl: ''
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
    async onSubmit({app}) {
      const response = await axios.post('idol_token/iregister_idol?name=test&address=0x227803804140ace3287C6fe824B8192f2ec060c0', {
        baseURL: 'https://idol-token-web.herokuapp.com/',
        headers: { "Content-Type": "application/json", 'X-Requested-With': 'XMLHttpRequest' },
        responseType: 'json',
        data: {}
      })
      // const response = await axios.post(
      //   'https://idol-token-web.herokuapp.com/idol_token/register_idol/', {
      //     params: {
      //       name: 'test',
      //       address: 'test'
      //     }
      //   }
      // )
      console.log(response.data)
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
      this.image = file;
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('Avatar picture must be JPG format!');
      }
      if (!isLt2M) {
        this.$message.error('Avatar picture size can not exceed 2MB!');
      }
      return isJPG && isLt2M;
    }
  }
}
</script>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>