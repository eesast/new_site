<template>
  <div class="hello">
    <el-carousel :interval="10000" height="650px">
      <el-carousel-item id="teamstyle1">
        <img src="../../static/teamstyle19.jpg">
      </el-carousel-item>
      <el-carousel-item id="teamstyle2">
        <img src="../../static/teamstyle-2.png">
      </el-carousel-item>
      <el-carousel-item id="software">
        <img src="../../static/software-contest.png">
      </el-carousel-item>
      <el-carousel-item id="edc">
        <img src="../../static/edc.jpg">
      </el-carousel-item>
    </el-carousel>
    <el-container>
      <!--el-aside width="30%">
        <h2>我们的部门</h2>
        <el-card class="box-card">
            <img src="../../static/cultivation.png"/>
          <p>学培部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/software.png"/>
            <p>软件部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/hardware.png"/>
            <p>硬件部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/project.png"/>
            <p>项目部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/scheme.png"/>
            <p>宣策部</p>
        </el-card>
      </el-aside-->

      <el-main>

        <el-row>
          <img src="../../static/activity.jpg"/>
          <div class="theme-disc">
            <h3>活动</h3>
            <p>活动</p>
            <el-button><h2>了解更多</h2></el-button>
          </div>    
        </el-row>

        <el-row>
          <img src="../../static/sast-weekly.jpg"/>
          <div class="theme-disc">
            <h3>EESAST-Weekly</h3>
            <p>EESAST-Weekly</p>
            <el-button><h2>了解更多</h2></el-button>
          </div>    
        </el-row>

        <el-row>
          <img src="../../static/activity.jpg"/>
          <div class="theme-disc">
            <h3>讲座</h3>
            <p>讲座</p>
            <el-button><h2>了解更多</h2></el-button>
          </div>    
        </el-row>

      </el-main>

    </el-container>
    <div id="depart-ctr">
      <h2>我们的部门</h2>
      <el-main id="department">
        
        <el-card class="box-card">
            <img src="../../static/cultivation.png"/>
          <p>学培部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/software.png"/>
            <p>软件部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/hardware.png"/>
            <p>硬件部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/project.png"/>
            <p>项目部</p>
        </el-card>
        <el-card class="box-card">
            <img src="../../static/scheme.png"/>
            <p>宣策部</p>
        </el-card>
      </el-main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*@import url("//unpkg.com/element-ui@2.3.4/lib/theme-chalk/index.css");*/

h1, h2 {
  font-weight: normal;
}

.el-carousel {
  background: black;
}

.el-carousel__item {
  width: 64%;
  margin: 0 18%;
}

.box-card {
  width: 80%;
  margin: 12px 10px;
  text-align: center;
}

.box-card img{
  width: 10%;
  margin: 0;
  min-width: 30px;
}

.box-card p{
  text-indent: 0;
}
.box-card:hover{
  opacity: 0.7;
  cursor: pointer;
}

.el-main#department {
  display: flex;
  width: 80%;
  margin: 0 auto;
}

.el-row {
  align-items: center;
  display: flex;
  margin: 0.5% 0;
  padding: 1% 0;
  border-style: none;
  border-radius: 10px;
  
}
.el-row img {
    width: 60%;
    margin: 0;
  }

  .theme-disc{
    align-items: center;
    margin: auto;
  }
  .theme-disc h3, .theme-disc p {
    text-indent: 0;
  }

  .el-button {
    margin: 80px auto;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
h3{
  font-size: 4em;
}
</style>
