<template>
  <div class="container">
    <div>
        {{name}}
    </div>
  </div>
</template>

<script>
export default {
    asyncData() {
        let idol = {id: 1, name: '田中麻美', image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'};

        return idol
    }
}
</script>
