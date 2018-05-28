<template>
    <div class='wrap'>
        <intro-title i-title='硬件设计大赛'></intro-title>
        <div class='content'>
            <div class='article'>
                <h4>赛事时间</h4>
                <p>
                   硬件设计大赛在每年【暑假小学期】举办，大概持续两周时间。 
                </p>
                <h4>赛事简介</h4>
                <p>
                    硬件设计大赛是清华大学电子系主办的一个比赛，主要面向电子系零基础的同学，赛前有若干次培训讲座，现场发放相应的模块，带领大家从零开始接触、学习单片机的基本操作，旨在激发同学们对硬件的热情。
                </p>
                <h4>精彩回顾</h4>
                <p>2017年硬件设计大赛作品：</p>
                <img src='../../../static/img/hdc-1.jpg'/>
                <img src='../../../static/img/hdc-2.jpg'/>
                <img src='../../../static/img/hdc-3.jpg'/>
                <img src='../../../static/img/hdc-4.jpg'/>
            </div>
        </div>
    </div>
</template>

<script>
import '../../../static/css/article.css';
import IntroTitle from './IntroTitle';
export default {
  name: 'hdc',
  components: { IntroTitle },
}
</script>