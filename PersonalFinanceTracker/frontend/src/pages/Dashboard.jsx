import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

function Dashboard() {
  const [summary, setSummary] = useState({ income: 0, expense: 0 });

  useEffect(() => {
    axios.get('/api/summary').then(res => setSummary(res.data));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">Monthly Summary</h2>
      <div className="my-4">Income: ₹{summary.income}</div>
      <div className="my-4">Expense: ₹{summary.expense}</div>
      <Bar
        data={{
          labels: ['Income', 'Expense'],
          datasets: [{
            label: 'Amount',
            data: [summary.income, summary.expense],
            backgroundColor: ['#4ade80', '#f87171']
          }]
        }}
      />
    </div>
  );
}

export default Dashboard;