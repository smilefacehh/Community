// pages/index/index.js
import {
  formateDate,
  getWeekday
} from '../../utils/date_util'

Page({

  // 页面初始数据
  data: {
    actionList: [],
    weightUnitList: ['kg', 'lbs'],
    countPickerNums: [0,1,2,3,4,5,6,7,8,9,10],
    chooseActionBodyId: -1,
    chooseActionId: -1
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // todo:日期应该从服务器获取，获取网络时间
    let curr_date = new Date();
    let date_str = formateDate(curr_date, "Y-M-D");
    let weekday_str = getWeekday(curr_date);

    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/train/actions/',
      data: {
        userid: 1
      },
      method: 'GET',
      success: function (res) {
        console.log(res.data)
        that.setData({
          actionList: res.data['content']
        })
      }
    })
  },

  // 添加一个动作
  onClickAddAction(){
    wx.navigateTo({
      url: '/pages/actions/actions',
    })
  },

  // onShow: function () {
  //   let choose_action_body_id = this.data.chooseActionBodyId;
  //   let choose_acction_id = this.data.chooseActionId;
  //   if(choose_action_body_id != -1 && choose_acction_id != -1){
  //     let new_body = {
  //       text: '腿',
  //       actionList: [
  //         {
  //           name: '深蹲',
  //           img: '/images/icon-pic.png',
  //           countList: [
  //             {
  //               weight: 20,
  //               count: 10,
  //               unit: 'kg'
  //             }
  //           ]
  //         }
  //       ]
  //     };
  //     let body_list = this.data.bodyList;
  //     body_list.push(new_body);
  //     this.setData({
  //       bodyList: body_list
  //     })
  //   }
  //   console.log(choose_action_body_id);
  //   console.log(choose_acction_id);
  //   this.setData({
  //     chooseActionBodyId: -1,
  //     chooseActionId: -1
  //   })
  // }
})