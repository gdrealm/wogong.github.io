title: 迁移至 Amazon S3 
date: 2015-07-07 10:24:05
modified: 2015-07-07 10:24:05
category: 
tags: 
slug: to-amazon-s3
authors: wogong
summary: 静态博客托管迁移至AWS S3 Service

最开始在网上的页面是 vimwiki，之后转移到 Jekyll，基本一直托管在 Github，可恨 Jekyll 对于中文的支持直到 3.0 版本都没有任何改观，所以前段时间简单折腾转移到 Pelican，目前的静态博客生成工具非常多，相比 Jekyll，Pelican 于我而言最大的优势是对中文的支持较为友好，另外 Python 环境相比 Ruby 而言，折腾起来较为简单。当然，游走于各种环境只是为了折腾，和书写其实没有太大关系，也和文题无关。

静态博客最大的优势怕是在于托管的方便了，国内的 空间/CDN/VPS 由于备案制度的存在，不予考虑。Github Pages 的托管其实是最优的选择，廉价的 VPS 无论是稳定性还是速度都不尽如人意，且需要牵扯较大的精力维护，与博客的初衷相去甚远，Linode 之类的优质 VPS 虽然基本不存在稳定和速度的问题，但是于我仅仅用来挂个静态的博客，又显得奢侈。Github Pages 一方面是墙的问题，虽然这一点个人不是太在意，但是在 Code Repo 里放一堆丑陋的 Pelican 生成的 HTML 文件实在是不能忍受。可以说是蓄谋已久，也可以说是心血来潮，总之，用了办个上午的时间搬家到了 Amazon S3 Service.

Amazon S3 Service 是 AWS 服务的一项，AWS 需要信用卡开通，新用户有一年的免费试用时间。S3 的价格非常便宜，作为静态博客托管基本可以不考虑费用:)

官方提供了详细的静态网站托管流程：[使用自定义域设置静态网站](https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)
但是个人采用的方案和上述流程有一些区别，例如域名解析上述流程采用  Route 53，一些关于权限和域名绑定的小问题记录如下。

### 权限设置（利用 ref4 AWS Policy Generator 生成）：

    {
	    "Version": "2012-10-17",
    	"Id": "Policy1436229520943",
	    "Statement": [
    		{
			    "Sid": "AllowPublicRead",
		    	"Effect": "Allow",
	    		"Principal": "*",
    			"Action": "s3:*",
			    "Resource": "arn:aws:s3:::wogong.net/*"
		    }
	    ]
    }

### 域名绑定：Dnsimple

    ALIAS   wogong.net      www.wogong.net.s3-website-ap-northeast-1.amazonaws.com
    CNAME   www.wogong.net  www.wogong.net.s3-website-ap-northeast-1.amazonaws.com

### 重定向规则
为 HTTP 错误进行重定向

      <RoutingRules>
        <RoutingRule>
        <Condition>
          <HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals >
        </Condition>
        <Redirect>
          <HostName>wogong.net</HostName>
          <ReplaceKeyWith>404.html</ReplaceKeyWith>
        </Redirect>
        </RoutingRule>
      </RoutingRules>


下一步要折腾的就是 CDN 了，Amazon CloudFront 服务正在申请中

reference:
1. [怎样用linux命令行访问AmazonS3云存储](http://www.geekfan.net/7935/)
2. [使用 HTTPS 连接访问您的对象](https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html)
3. <https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html> 
4. [AWS Policy Generator](http://awspolicygen.s3.amazonaws.com/policygen.html)

