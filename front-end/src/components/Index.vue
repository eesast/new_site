<template>
  <div class="hello">
    <el-carousel :interval="10000" type="card" height="500px">
      <el-carousel-item id="teamstyle1">
        <img src="../../static/teamstyle.png">
      </el-carousel-item>
      <el-carousel-item id="teamstyle2">
        <img src="../../static/teamstyle-2.png">
      </el-carousel-item>
      <el-carousel-item id="software">
        <img src="../../static/software.png">
      </el-carousel-item>
      <el-carousel-item id="edc">
        <img src="../../static/edc.jpg">
      </el-carousel-item>
    </el-carousel>
    <el-container>
      <el-aside width="30%">
        <h2>我们的部门</h2>
        <el-card class="box-card">
          <div>
            <i class="el-icon-document"></i>
            <p>学培部</p>
          </div>
        </el-card>
        <el-card class="box-card">
          <div>
            <i class="el-icon-document"></i>
            <p>软件部</p>
          </div>
        </el-card>
        <el-card class="box-card">
          <div>
            <i class="el-icon-document"></i>
            <p>硬件部</p>
          </div>
        </el-card>
        <el-card class="box-card">
          <div>
            <i class="el-icon-document"></i>
            <p>项目部</p>
          </div>
        </el-card>
        <el-card class="box-card">
          <div>
            <i class="el-icon-document"></i>
            <p>宣策部</p>
          </div>
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
              <img src="../assets/logo.png">
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
              <img src="../assets/logo.png">
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content learn">
              <el-button>了解更多</el-button>
            </div>
          </el-col>
        </el-row>
        <!--el-row>
          <el-col :span="8">
            <div class="grid-content">
              <el-button>了解更多</el-button>
            </div>
          </el-col>
          <el-col :span="16">
            <div class="grid-content light-blue">
              <img src="../assets/logo.png">
              <div class="theme-disc">
                <h3>活动</h3>
                <p>活动</p>
              </div>
              
            </div>
          </el-col>
        </el-row-->

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
i {
  width: 50px;
}

.el-carousel {
  background: black;
}

.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item#teamstyle1 {
    background-color: #d3dce6;
  }
  .el-carousel__item#teamstyle1 img{
    width: 70%;
  }

.box-card {
  width: 80%;
  margin: 15px auto;
}

.box-card div{
  text-align: center;
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

a {
  color: #42b983;
}
</style>
