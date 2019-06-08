<template>
  <div class="container">
      <el-row>
          <img :src="image" class="image">
      </el-row>
    <div>
        {{name}}
    </div>
  </div>
</template>

<script>
export default {
    asyncData() {
        let idol = {id: 1, name: '田中麻美', image: 'https://i.ytimg.com/vi/Ti6l8JD1PBY/maxresdefault.jpg'};

        return idol
    }
}
</script>

<style>
    .image {
        width: 100%;
        height: auto;
    }
</style>

