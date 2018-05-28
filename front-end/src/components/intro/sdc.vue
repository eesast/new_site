<template>
    <div class='wrap'>
        <intro-title i-title='软件设计大赛'></intro-title>
        <div class='content'>
            <div class='article'>
                <h4>简要介绍</h4>
                <p>
                    软件设计大赛要求参赛者使用当今主流的技术栈，面向某个特定需求，完成一套具备一定可用性和美观性的软件程序。
                    对于“软件”的定义十分宽泛，游戏、网站、APP 都可以作为作品提交。
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import '../../../static/css/article.css';
import IntroTitle from './Introtitle';
export default {
    name: 'sdc',
    components: { IntroTitle },
}
</script>