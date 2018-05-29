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
      <el-aside width="30%">
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
      </el-aside>

      <el-main>

        <el-row>
          <el-col :span="16">
            <div class="grid-content light-blue">
              <div class="theme-disc">
                <h3>活动</h3>
                <p>活动</p>
              </div>
              <img src="../../static/activity.jpg">
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content learn">
              <el-button>了解更多</el-button>
            </div>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="16">
            <div class="grid-content light-blue">
              <div class="theme-disc">
                <h3>SAST-Weekly</h3>
                <p>SAST-Weekly</p>
              </div>
              <img src="../../static/sast-weekly.jpg">
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content learn">
              <el-button>了解更多</el-button>
            </div>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="16">
            <div class="grid-content light-blue">
              <div class="theme-disc">
                <h3>讲座</h3>
                <p>讲座</p>
              </div>
              <img src="../assets/logo.png">
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content">
              <el-button>了解更多</el-button>
            </div>
          </el-col>
        </el-row>

      </el-main>
    </el-container>
  
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
  margin: 12px auto;
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

.el-row {
    margin-bottom: 20px;
  }
  .el-col {
    border-radius: 4px;
  }
  .el-col img {
    margin: 0 10%;
    width: 30%;
  }
  .el-button {
    margin: 80px auto;
  }
  .light-blue {
    background: rgb(104,202,255,0.3);
  }
  .theme-disc {
    align-items: center;
    margin: 0 auto;
    padding: 0;
  }
  .grid-content {
    display:flex;
    border-radius: 4px;
    min-height: 36px;
    align-items: center;
  }

  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }

</style>
