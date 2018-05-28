<template>
  <div>

    <el-menu
  :default-active="activeIndex2"
  class="el-menu-demo"
  mode="horizontal"
  @select="handleSelect"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#ffd04b">
  <div class="top">
    <img src="..\..\static\eesast.png">
    <div id="title">
      <h2>清华大学电子工程系学生科协</h2>
      <h3>Student Association of Science and Technology</h3>
    </div>
    
  </div>
  <el-menu-item index="1" route="">首页</el-menu-item>
  <el-submenu index="2" route="">
    <template slot="title" route="">部门</template>
    <el-menu-item index="2-1" route="">学培部</el-menu-item>
    <el-menu-item index="2-2" route="">软件部</el-menu-item>
    <el-menu-item index="2-3" route="">硬件部</el-menu-item>
    <el-menu-item index="2-4" route="">项目部</el-menu-item>
    <el-menu-item index="2-5" route="">宣策部</el-menu-item>
    <!--el-submenu index="2-4">
      <template slot="title">选项4</template>
      <el-menu-item index="2-4-1">选项1</el-menu-item>
      <el-menu-item index="2-4-2">选项2</el-menu-item>
      <el-menu-item index="2-4-3">选项3</el-menu-item>
    </el-submenu-->
  </el-submenu>
  <el-submenu index="3">
    <template slot="title" route="">赛事</template>
    <el-menu-item index="3-1" route="">队式设计大赛</el-menu-item>
    <el-menu-item index="3-2" route="">电子设计大赛</el-menu-item>
    <el-menu-item index="3-3" route="">硬件设计大赛</el-menu-item>
    <el-menu-item index="3-4" route="">挑战杯</el-menu-item>
    <el-menu-item index="3-5" route="">ADI杯新生知识竞赛</el-menu-item>
  </el-submenu>
  <el-menu-item index="4" route="">SAST-Weekly</el-menu-item>
  <el-menu-item index="5">注册</el-menu-item>
  <el-menu-item index="6">登录</el-menu-item>
  </el-menu>
  </div>
</template>

<script>
export default {
    name: 'navbar',
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style scoped>
.top {
    display: flex;
}
.top img{
  width: 5%;
  height: 5%;
  margin: 0;
}
div#title{
  text-align: left;
  padding-left: 1%;
}
#title h2,#title h3{
  margin: 1% 0;
  color: white;
}

</style>
