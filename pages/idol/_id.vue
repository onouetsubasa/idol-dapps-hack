<template>
<div class="container">
  <el-table
    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%">
    <el-table-column
      label="Date"
      prop="date">
    </el-table-column>
    <el-table-column
      label="Name"
      prop="name">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot-scope="scope">
        <el-button type="primary" @click="onSubmit">発行</el-button>
        <el-button type="primary" icon="el-icon-lollipop">購入</el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>
<script>
import Web3 from 'web3'
import abi from '~/plugins/abi'
// import contract_addr from '~/plugins/contract_addr'
var web3

// init client web3 js
if (process.browser) {
  console.log('givenProvider=')
  console.log(Web3.givenProvider)
  web3 = new Web3(Web3.givenProvider)
}

// const contract = new web3.eth.Contract(abi, '0xe228f3388ac5aaf4a81f9af358ac5dae6bb13028')
let a = process.env.contract_addr
const contract = new web3.eth.Contract(abi, process.env.contract_addr)


  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-03',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles'
        }, {
          date: '2016-05-02',
          name: 'John',
          address: 'No. 189, Grove St, Los Angeles'
        }, {
          date: '2016-05-04',
          name: 'Morgan',
          address: 'No. 189, Grove St, Los Angeles'
        }, {
          date: '2016-05-01',
          name: 'Jessy',
          address: 'No. 189, Grove St, Los Angeles'
        }],
        search: '',
      }
    },
  methods: {
    handleChange(value) {
      console.log(value)
    },
    onSubmit() {
    //   contract.methods.mintvoice(
    //     1
    //   )

      contract.methods.releaseVoice(
        9999,
        this.form.supply,
        this.form.price
      )
      .send({
          from: this.address,
          gas: 30000000,
          gasPrice: '3000000'
      }, (error, transactionHash) => {
        console.log(transactionHash)
      })
      .on('transactionHash', (hash) => {
        this.transaction = hash
      })
      .on('confirmation', (confirmationNumber, receipt) => {
        if(receipt.status) {
          this.$router.push({ path: `/idol/${receipt.from}` })
        }
      })
    }
  }
  }
</script>