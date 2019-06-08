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
  <el-table
    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%">
    <el-table-column
      label="Date"
      prop="date">
    </el-table-column>
    <el-table-column
      label="Name"
      prop="name">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-video-play" @click="onPlay"></el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>
<script>
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-03',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles'
        }, {
          date: '2016-05-02',
          name: 'John',
          address: 'No. 189, Grove St, Los Angeles'
        }, {
          date: '2016-05-04',
          name: 'Morgan',
          address: 'No. 189, Grove St, Los Angeles'
        }, {
          date: '2016-05-01',
          name: 'Jessy',
          address: 'No. 189, Grove St, Los Angeles'
        }],
        search: '',
      }
    },
    methods: {
      onPlay() {
        new Audio('/Users/takasetoshiaki/Desktop/music.mp3').play();
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