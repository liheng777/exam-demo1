<template>
    <div class="about">
        <div id="container">
            <canvas id="chart" />
        </div>
    </div>
</template>
<script>
import Chart from '@blueking/bkcharts'
export default {
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    const context = document.getElementById('chart')
    this.chart = new Chart(context, {
      type: 'bar',
      data: {
        labels: [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December'
        ],
        datasets: [
          {
            backgroundColor: 'rgba(51,157,255,1)',
            borderColor: 'rgba(51,157,255,1)',
            borderSkipped: 'bottom',
            borderWidth: 1,
            clip: '',
            data: [65, 90, 10, 15, 69, 47, 100, 55, 88, 66, 22, 11],
            label: 'Rainfall'
          }
        ]
      },
      options: {
        responsive: true,
        legend: { position: 'top' },
        title: { display: true, text: '基础柱状图' },
        scales: {
          yAxes: {
            scaleLabel: { display: true, labelString: 'Precipitation in mm' }
          },
          xAxes: { scaleLabel: { display: true, labelString: 'Month of the Year' } }
        }
      }
    })
  }
}
</script>
