// pages/history/history.js

Page({

  /**
   * 页面的初始数据
   */
  data: {
    columns: ['杭州', '宁波', '温州', '嘉兴', '湖州'],
    bodyList: [
      {
        name: '胸',
        instList: [
          {
            name: '杠铃',
            actionList: [
              {
                name: '杠铃卧推',
                img: '/images/action-wotui.png'
              },
              {
                name: '宽距杠铃卧推',
                img: '/images/action-wotui.png'
              }
            ]
          },
          {
            name: '哑铃',
            actionList: [
              {
                name: '哑铃卧推',
                img: '/images/action-wotui.png'
              },
              {
                name: '平躺哑铃卧推',
                img: '/images/action-wotui.png'
              }
            ]
          },
        ]
      },
      {
        name: '背',
        instList: [
          {
            name: '杠铃',
            actionList: [
              {
                name: '杠铃划船',
                img: '/images/action-wotui.png'
              },
              {
                name: '反手杠铃划船',
                img: '/images/action-wotui.png'
              }
            ]
          },
          {
            name: '哑铃',
            actionList: [
              {
                name: '哑铃划船',
                img: '/images/action-wotui.png'
              },
              {
                name: '站姿哑铃划船',
                img: '/images/action-wotui.png'
              }
            ]
          },
        ]
      }
    ]
  },

  onChange(event) {
    const {
      picker,
      value,
      index
    } = event.detail;
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})