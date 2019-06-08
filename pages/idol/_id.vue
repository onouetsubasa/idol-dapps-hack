<template>
<div class="container">
  <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      label="名前"
      prop="">
    </el-table-column>
    <el-table-column
      label="最大発行量"
      prop="totalSupply">
    </el-table-column>
    <el-table-column
      label="発行済み"
      prop="issuedNum">
    </el-table-column>
    <el-table-column
      label="金額"
      prop="price">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-lollipop">購入</el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>

<script>
import Web3 from 'web3'
import abi from '../../plugins/abi'
var web3

// init client web3 js
if (process.browser) {
  console.log('givenProvider=')
  console.log(Web3.givenProvider)
  web3 = new Web3(Web3.givenProvider)
}

const contract = new web3.eth.Contract(abi, '0xfd55cdf84a5545971341f17e4746cd300301aee3')

  export default {
    data() {
      return {
        tableData: []
      }
    },
    async created() {
      contract.methods.balanceOfOwnedVoices(
        this.$route.params.id
      ).call()
      .then((result) => {
        const num = web3.utils.hexToNumber(result)
        for(var i=0; i < num; i++) {
          contract.methods.ownedVoices(
            this.$route.params.id,
            i
          ).call()
          .then((result) => {
            const voiceId = web3.utils.hexToNumber(result)
            contract.methods.voices(
              voiceId
            ).call()
            .then((result) => {
              const totalSupply = web3.utils.hexToNumber(result.totalSupply)
              const issuedNum = web3.utils.hexToNumber(result.issuedNum)
              const price = web3.utils.hexToNumber(result.price)
              console.log({
                totalSupply: totalSupply,
                issuedNum: issuedNum,
                price: price
              })
              this.tableData.push({
                totalSupply: totalSupply,
                issuedNum: issuedNum,
                price: price
              })
            })
          })
        }
      })
    },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    },
  }
</script>