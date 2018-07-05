#-*- coding:utf-8 -*-

# 配置
config = {
    "width" : 150,   # 画布宽度
    "height" : 100,  # 画布高度
    "frame" : 10,    # 播放的帧率
    "ratio" : 1.0,   # 图像缩放的比率
}

# 网页css样式
Style = '''
<style>
    .div-a > pre {font-size : 6px; line-height : 2px; }
    .div-a {float : left; width : 69%;}
    .div-b {float : left; width : 29%;}
</style>
'''

# javascript代码，逐个显示pre里面的字符
JavaScript = '''
<script>
    window.onload = function(){
        var frames = document.getElementsByTagName('pre');
        var length = frames.length;
        var current = 0;
        var doframe = function() {
            frames[current].style.display = 'block';
            frames[(current - 1 + length) %% length].style.display = 'none';
            current = (current + 1) %% length;
        }
        for (var i = 0; i < length; i++)
            frames[i].style.display = 'none';
        setInterval(doframe, 1000/%d)
    }
</script>
''' % config['frame']