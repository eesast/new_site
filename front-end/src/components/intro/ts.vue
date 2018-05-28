<template>
<div class='wrap'>
    <intro-title i-title='队式程序设计大赛'></intro-title>
    <div class='content'>
        <div class='article'>
            <h4>赛事时间</h4>
            <p>队式程序设计大赛在【春季学期】举行。在激烈的赛程之前，会有电子系科协举办的培训讲座，帮助选手们快速上手，参与进紧张有趣的赛程中，感受AI的编程之美。
            </p>
            <h4>赛事简介</h4>
            <p>“队式程序设计大赛”是由清华大学电子系科协举办的一项经典赛事，是一个组队参加的对抗性策略程序设计比赛。比赛主题往往基于某款经典电子游戏，设计出的全新规则，邀请选手组队设计出更加完善和智能的游戏策略，并用高效的程序代码实现。比赛往往以双方AI对战的形式进行，决赛时还会使用3D界面向全场播送比赛实况，对抗性和观赏性极强，为清华大学内一年一度的程序设计盛事。
            </p>
            <h4>赛事精彩回顾</h4>
            <div class="img-wrap">
                <img src='../../../static/img/ts-1.png'/>
                <p class='ia'>队式十六——深蓝(Deep Blue)</p>
            </div>
            <div class="img-wrap">
                <img src='../../../static/img/ts-2.png'/>
                <p class='ia'>队式十七——Stellar craft</p>
            </div>
            <div class="img-wrap">
                <img src='../../../static/img/ts-3.png'/>
                <p class='ia'>2018年，队式十九作为A1组比赛合并到THU-AI中</p>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import '../../../static/css/article.css';
import IntroTitle from './IntroTitle';
export default {
  name: 'ts',
  components: { IntroTitle },
}
</script>
