---
layout: post
title: "如何在Symfony2中创建终端命令"
description: ""
category: it
tags: [Symfony2, Command, Console]
---

详情请参见[官方文档](http://symfony.com/doc/2.0/cookbook/console/console_command.html<F12>)

## 自动注册的终端命令

为了在sf2的终端中使用自定义的命令，我们需要在bundle路径下新建一个`Command`路径，在此路径下，为你需要的命令新建后缀为`Command.php`的文件，例如: 如果你希望在AcmeDemoBundle添加一个在终端访问你的功能。新建一个`GreetCommand.php`的文件，内容如下：

    //src/Acme/DemoBundle/Command/GreetCommand.php
    namespace Acme\DemoBundle\Command;
    
    use Symfony\Bundle\FrameworkBundle\Command\ContainerAwareCommand;
    use Symfony\Component\Console\Input\InputArgument;
    use Symfony\Component\Console\Input\InputInterface;
    use Symfony\Component\Console\Input\InputOption;
    use Symfony\Component\Console\Output\OutputInterface;
    
    class GreetCommand extends ContainerAwareCommand
    {
        protected function configure()
        {
            $this
                ->setName('demo:greet')
                ->setDescription('Greet someone')
                ->addArgument('name', InputArgument::OPTIONAL, 'Who do you want to greet?')
                ->addOption('yell', null, InputOption::VALUE_NONE, 'If set, the task will yell in uppercase letters')
            ;
        }
    
        protected function execute(InputInterface $input, OutputInterface $output)
        {
            $name = $input->getArgument('name');
            if ($name) {
                $text = 'Hello '.$name;
            } else {
                $text = 'Hello';
            }
    
            if ($input->getOption('yell')) {
                $text = strtoupper($text);
            }
    
            $output->writeln($text);
        }
    }
    

命令在终端就可以运行：

    >$ app/console demo:greet yourname



## 从serveice container中调用service

示例代码如下：

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $name = $input->getArgument('name');
        $translator = $this->getContainer()->get('translator');
        if ($name) {
            $output->writeln($translator->trans('Hello %name%!', array('%name%' => $name)));
        } else {
            $output->writeln($translator->trans('Hello!'));
        }
    }
 
## 在命令行发送邮件

如果你使用了memory spooling，那么子啊终端命令中调用时可能会没有办法发送邮件。因为在这种情况下，symfony不会自动发送邮件，你需要自己手动flushing，添加以下代码即可解决：

    $container = $this->getContainer();
    $mailer = $container->get('mailer');
    $spool = $mailer->getTransport()->getSpool();
    $transport = $container->get('swiftmailer.transport.real');
    $spool->flushQueue($transport);

参考官方文档：[http://symfony.com/doc/2.0/cookbook/console/sending_emails.html](http://symfony.com/doc/2.0/cookbook/console/sending_emails.html)

