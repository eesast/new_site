<template>
    <div class='wrap'>
        <intro-title i-title='电子设计大赛'></intro-title>
        <div class='content'>
            <div class='article'>
                <h4>赛事时间</h4>
                <p>
                    电子设计大赛在每年的【秋季学期】举行，从报名领取元件到决赛整个过程大概会持续半个学期，包括赛前培训，预赛初赛决赛等阶段，让同学们从机械结构到电路设计，从控制逻辑到上层策略，一步步完成作品。
                </p>
                <h4>赛事简介</h4>
                <p>
                    “电子设计大赛”是由清华大学电子系和自动化系合办的面向全校的比赛，选手可以组成不多于四人的队伍报名参加比赛。比赛一般是要求选手设计一辆智能车，根据赛题内容设计机械结构，编写单片机代码，实现自动控制。比赛形式是让两支队伍的智能车进行对抗，根据规则，胜者晋级，比赛过程中智能车除了根据传感器检测场地情况之外，还可以通过官方提供的通信模块从上位机处获取信息或者给上位机发送指令；决赛在罗姆楼进行，每年都会吸引大批观众，一边欣赏紧张激烈的比赛，一边听着激情洋溢的解说，见证冠军的诞生。
                </p>
                <h4>精彩回顾</h4>
                <div class='img-wrap'>
                    <img src='../../../static/img/edc.jpg'/>
                    <p class='ia'>第十八届电子设计大赛——天赐良机</p>
                </div>
                <div class='img-wrap'>
                    <img src='../../../static/img/edc19.jpg'/>
                    <p class='ia'>第十九届电子设计大赛——绿茵荣耀</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import '../../../static/css/article.css';
import IntroTitle from './IntroTitle';
export default {
  name: 'edc',
  components: { IntroTitle },
}
</script>
<style scoped>
@import '../../../static/css/article.css';
</style>
