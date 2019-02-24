<template>
  <div class="hello">
    <div>
    <b-carousel
      id="carousel1"
      style="text-shadow: 1px 1px 2px #333;"
      fade="true"
      controls
      indicators
      background="#222831"
      :interval="4000"
      img-width="1024"
      img-height="480"
      v-model="slide"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="Big Family"
        text="A Group of Intersting People"
        img-src="../../static/index/index-1.png"
      />

      <!-- Slides with custom text -->
      <b-carousel-slide img-src="../../static/index/index-4.png" >
        <h1>Tsinghua Electronic Competition</h1>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide img-src="../../static/index/index-2.png" >
        <h1>TeamStyle</h1>
      </b-carousel-slide>
      

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide img-src="../../static/index/index-3.png" >
        <h1>Software Design Competition</h1>
      </b-carousel-slide>

    </b-carousel>
  </div> 
    <div id="depart-ctr">
      <!-- </br>
      <h2>我们的部门</h2> -->
      <el-main id="department">
        <router-link to="intro/dep" class="link-to-study" @click.native="selectnav('dep study')">
          <el-card class="box-card"> 
            <img src="../../static/cultivation.png"/>
          <p>学培部</p>
          </el-card>
        </router-link>
        <router-link to="intro/dep" class="link-to-software" @click.native="selectnav('dep software')">
          <el-card class="box-card">
          
            <img src="../../static/software.png"/>
            <p>软件部</p>
          </el-card>
        </router-link>   
        <router-link to="intro/dep" class="link-to-hardware" @click.native="selectnav('dep hardware')">
          <el-card class="box-card">
              <img src="../../static/hardware.png"/>
            <p>硬件部</p>  
          </el-card>
        </router-link>
        <router-link to="intro/dep" class="link-to-project" @click.native="selectnav('dep project')">
          <el-card class="box-card">  
            <img src="../../static/project.png"/>
            <p>项目部</p>   
          </el-card>
        </router-link>
        <router-link to="intro/dep" class="link-to-department" @click.native="selectnav('dep propagate')">
          <el-card class="box-card">     
            <img src="../../static/scheme.png"/>
            <p>宣策部</p>   
          </el-card>
        </router-link>
      </el-main>
    </div>
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
          <img src="../../static/lecture.jpg"/>
          <div class="theme-disc">
            <h3>讲座</h3>
            <p>讲座</p>
            <el-button><h2>了解更多</h2></el-button>
          </div>    
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
      slide: 0,
      sliding: null,
      swiperOption: {//swiper3
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          },
          pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true
          },
        // effect: 'fade',
        loop: true,
        grabCursor: true,
      },
      msg: 'Welcome to Your Vue.js App',
    }
  },
  methods:
  {
    selectnav(selectindex)
    {
      // console.log(selectindex);
      let selectedindex=selectindex;
      localStorage.setItem('id',selectedindex);
    },
    onSlideStart(slide) {
        this.sliding = true
    },
    onSlideEnd(slide) {
        this.sliding = false
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
  background:black;
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

#department a
{
  text-decoration:none;
  width:100%;
}

.box-card img{
  width: 10%;
  margin: 0;
  min-width: 30px;
}

.box-card p{
  text-indent: 0;
  color:black;
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

.swiper-slide {
    width: 80%;
    height: 50%;
    /* background-position: center; */
    /* background-size: cover; */
    background-color: black;
}




</style>
