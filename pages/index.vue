<template>
  <div class="container">
    <div>
      <el-row>
        <el-col :span="4" v-for="i in idols" :key="i.id">
          <el-card :body-style="{ padding: '10px' }">
            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
            <div style="padding: 14px;">
              <span>Yummy hamburger</span>
              <div class="bottom clearfix">
                <time class="time">{{ currentDate }}</time>
                <el-button type="text" class="button">Operating</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'

let idol = {
  name: '',
  image: ''
}

let idol1 = {id: 1, name: '田中麻美', image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'};
let idol2 = {id: 2, name: 'さとうひよこ', image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'};
let idol3 = {id: 3, name: '田中麻美', image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'};
let idol4 = {id: 4, name: 'さとうひよこ', image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'};

let idolArr = [idol1, idol2, idol3, idol4]

export default {
  components: {
    Logo
  },
  asyncData() {

    let data = {idols: idolArr}
    return data
  }
}
</script>

<style>
  .time {
    font-size: 13px;
    color: #999;
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

