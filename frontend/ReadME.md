# 记录
```
1.列表动态删除input条目，发现数据渲染不更新
<input value="{{item.weight}}">需要加上value属性
2.索引动态列表中的某一条目
data-id="{{index}}"
let index = e.currentTarget.dataset.id;
```

# 使用三方组件
```
需要安装node.js, npm

vant/weapp
1.在frontend目录下执行npm init，一路回车，会生成一个package.json文件
2.npm i @vant/weapp -S --production
3.目录下会生成node_modules，包含组件内容
4.工具-构建npm，会生成miniprogram_npm目录
5.使用这个目录路径
```

# 调试
```
真机调试卡顿问题
真机打开小程序，点击右上角三个点，点击打开调试，然后关闭小程序重新打开，就不卡了，离线模式。应该是本地调试了，没有服务器通信
```

# 训练页数据
```
{
  actionList: [ // 训练动作列表
    {
      name: '胸', // 部位
      actions: [ // 动作列表
        {
          name: '杠铃推胸', // 动作名称
          img: '/images/icon-pic.png' // 图片地址
          records: [ // 组数重量记录列表
            {
              type: 0, // 0表示正常组，1表示热身组
              group_idx: 1 // 组索引
              weight: 10, // 重量
              count: 10, // 次数
              unit: 0, // 0表示kg，1表示磅lbs
            }
          ]
        }
      ]
    }
  ],
  // 饮食记录列表
  foodList: [
    {
      name: '米饭',
      hit: 0, // 热量
      fat: 0, // 脂肪
      protain: 0, // 蛋白质
      carbon: 0 // 碳水
    }
  ]
}
```