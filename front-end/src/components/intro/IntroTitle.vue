<template>
  <div class="wrap">
    <div class="title">
      <h3>{{ iTitle }}</h3>
    </div>
  </div>
</template>
<script>
export default {
  name:'intro',
  props: {
    iTitle:{
      type:String,
      default: '示例'
    }
  }
}
</script>

<style lang="scss" scoped>
$title-border: 1px;
.wrap {
  width: 100%;
  height: 80px;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  border-bottom: {
    width: 1px;
    color: rgb(221, 221, 221);
    style: solid;
  }
  box-shadow: 0 0 4px rgba(0,0,0,.14), 0 4px 8px rgba(0,0,0,.28);
}
.title {
  margin: 0 auto;
  height: 50px;
  transform:skewX(-30deg);
  box-sizing: content-box;
  order: 1;
  border-left: {
    style: solid;
    width: $title-border;
  }
  border-right: {
    style: solid;
    width: $title-border;
  }
}
h3 {
  margin: 0 auto;
  padding: 0 30px;
  font-size: 32px;
  height: 50px;
  line-height: 50px;
  transform: skewX(30deg);
  text-align: center;
  vertical-align: middle;
}
</style>
