<template>
  <div>

    <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#222831" text-color="#00ADB5" active-text-color="#00ADB5" router>
      <!--zdiv class="top">
        <div id="title">
          <h2>清华大学电子工程系学生科协</h2>
          <h3>Student Association of Science and Technology</h3>
        </div>
      </div-->    
      <el-menu-item index="0" id='img-submenu' route="/">
        <img class="eesast" src="..\..\static\eesast.png"/> <font id="text-eesast">EESAST</font>
      </el-menu-item>
      <el-menu-item index="2" route="/" id="home">首页</el-menu-item>
      <el-menu-item index="3" route="/intro/dep" @click.native="delstorage()" id="dep">部门</el-menu-item>
      
      <el-submenu index="4" id="comp">
        <template slot="title" route="/intro" id="popup">赛事</template>
        <el-menu-item index="4-1" route="/intro/ts">队式设计大赛</el-menu-item>
        <el-menu-item index="4-2" route="/intro/edc">电子设计大赛</el-menu-item>
        <el-menu-item index="4-3" route="/intro/hdc">硬件设计大赛</el-menu-item>
        <el-menu-item index="4-4" route="/intro/sdc">软件设计大赛</el-menu-item>
        <el-menu-item index="4-5" route="/intro/cc">挑战杯</el-menu-item>
        <el-menu-item index="4-6" route="/intro/ADI">新生知识竞赛</el-menu-item>        
      </el-submenu>
      <el-menu-item index="4" route="/intro/train" id="train">培训</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
    name: "navbar",
    data() {
        return {
            activeIndex: "1",
            activeIndex2: "1"
        };
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        delstorage()
        {
          // // console.log(selectindex);
          // let selectedindex=selectindex;
          // localStorage.setItem('id',selectedindex);
          localStorage.removeItem("id");
        }
    }
};
</script>

<style scoped>
.top {
    display: flex;
}
.eesast{
  height: 40px;
  width: 40px;
  margin: 10px 15px 10px 15px;
}
#img-submenu{
  border: none;
  cursor: default;
  background-color: #222831 !important;
}
#text-eesast{
  font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 200%;
  font-weight: 400;
  color:"#00ADB5";
}
ul, li {
  border: none;
  color: #00ADB5 !important;
  font-size: 14px !important;
  /* color: antiquewhite !important; */
}
.el-submenu__title
{
  border: none;
  color: #00ADB5 !important;

  /* color:antiquewhite !important; */
}
.el-menu {
  display: flex !important;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
#img-submenu {
  margin-right: calc(100vw - 530px);
}
.popup {
  padding: 0;
  margin: 0;
}
/* #train{
  right: 0;
  position: absolute;
} */
#home{
  right: 0;
  position: relative;
}

/*.el-menu--horizontal {
  height: 60px;
}
.top img {
    width: 5%;
    height: 5%;
    margin: 0;
}
div#title {
    text-align: left;
    padding-left: 1%;
}
#title h2,
#title h3 {
    margin: 1% 0;
    color: white;
}*/
</style>