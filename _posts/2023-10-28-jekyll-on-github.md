---
title: jekyll+github action搭建不完全指南
categories: 网站
---

github支持jekyll已久，但新推出的github action做到了每次推送后能使用ruby自动生成部署jekyll站点，与本地部署无异，可以使用所有的插件。

## fork jekyll主题

我用的是[chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)，克隆[chirpy-starter](https://github.com/cotes2020/chirpy-starter)仓库。

## 部署github actions

根据[jekyll官方文档](https://jekyllrb.com/docs/continuous-integration/github-actions/#setting-up-the-action)即可。

在仓库的Action tab中可以看到`Build and Deploy`和`Deploy Jekyll site to Pages`的结果，以及错误日志。