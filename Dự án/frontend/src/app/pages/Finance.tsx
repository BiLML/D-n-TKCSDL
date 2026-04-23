import { CreditCard, TrendingDown, Award } from 'lucide-react';

export function Finance() {
  const transactions = [
    {
      date: 'Apr 15, 2026',
      description: 'Spring 2026 Tuition',
      amount: -8500.0,
      status: 'Paid',
    },
    {
      date: 'Apr 10, 2026',
      description: 'Lab Fees - Computer Vision',
      amount: -150.0,
      status: 'Paid',
    },
    {
      date: 'Apr 5, 2026',
      description: 'Student Activity Fee',
      amount: -75.0,
      status: 'Paid',
    },
    {
      date: 'Mar 20, 2026',
      description: 'Technology Fee',
      amount: -200.0,
      status: 'Paid',
    },
    {
      date: 'Mar 15, 2026',
      description: 'Meal Plan Credit',
      amount: 500.0,
      status: 'Credited',
    },
  ];

  const scholarships = [
    {
      name: 'Academic Excellence Scholarship',
      amount: 5000.0,
      status: 'Active',
      period: 'Fall 2025 - Spring 2026',
    },
    {
      name: 'STEM Research Grant',
      amount: 2500.0,
      status: 'Active',
      period: 'Fall 2025 - Spring 2026',
    },
  ];

  const totalBalance = 0.0;

  return (
    <div className="grid grid-cols-3 gap-6">
      <div className="col-span-2">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm mb-6">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="mb-2">Account Balance</h3>
              <p className="text-gray-500">Current outstanding balance</p>
            </div>
            <div className="text-right">
              <p className="text-[#4F46E5]">${totalBalance.toFixed(2)}</p>
              {totalBalance > 0 && (
                <button className="mt-4 px-6 py-2 bg-[#4F46E5] text-white rounded-lg hover:bg-[#4338CA] transition-colors">
                  Pay Now
                </button>
              )}
              {totalBalance === 0 && (
                <p className="text-green-600 mt-2">Account Current</p>
              )}
            </div>
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div className="p-4 bg-[#F5F7FA] rounded-xl">
              <div className="flex items-center gap-2 mb-2">
                <CreditCard className="w-5 h-5 text-[#4F46E5]" />
                <span className="text-gray-600">Total Charges</span>
              </div>
              <p className="text-gray-900">$8,925.00</p>
            </div>

            <div className="p-4 bg-[#F5F7FA] rounded-xl">
              <div className="flex items-center gap-2 mb-2">
                <TrendingDown className="w-5 h-5 text-green-600" />
                <span className="text-gray-600">Total Payments</span>
              </div>
              <p className="text-gray-900">$8,925.00</p>
            </div>

            <div className="p-4 bg-[#F5F7FA] rounded-xl">
              <div className="flex items-center gap-2 mb-2">
                <Award className="w-5 h-5 text-[#4F46E5]" />
                <span className="text-gray-600">Financial Aid</span>
              </div>
              <p className="text-gray-900">$7,500.00</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h3 className="mb-6">Recent Transactions</h3>
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-[#E5E7EB]">
                  <th className="text-left py-3 px-4 text-gray-600">Date</th>
                  <th className="text-left py-3 px-4 text-gray-600">Description</th>
                  <th className="text-right py-3 px-4 text-gray-600">Amount</th>
                  <th className="text-center py-3 px-4 text-gray-600">Status</th>
                </tr>
              </thead>
              <tbody>
                {transactions.map((transaction, index) => (
                  <tr
                    key={index}
                    className="border-b border-[#E5E7EB] last:border-b-0 hover:bg-[#F5F7FA] transition-colors"
                  >
                    <td className="py-4 px-4 text-gray-600">{transaction.date}</td>
                    <td className="py-4 px-4 text-gray-900">{transaction.description}</td>
                    <td
                      className={`py-4 px-4 text-right ${
                        transaction.amount < 0 ? 'text-red-600' : 'text-green-600'
                      }`}
                    >
                      {transaction.amount < 0 ? '-' : '+'}$
                      {Math.abs(transaction.amount).toFixed(2)}
                    </td>
                    <td className="py-4 px-4 text-center">
                      <span
                        className={`px-3 py-1 rounded-full text-sm ${
                          transaction.status === 'Paid'
                            ? 'bg-green-100 text-green-700'
                            : 'bg-blue-100 text-blue-700'
                        }`}
                      >
                        {transaction.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div className="col-span-1">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h4 className="mb-4">Scholarships & Aid</h4>
          <div className="space-y-4">
            {scholarships.map((scholarship, index) => (
              <div
                key={index}
                className="p-4 bg-gradient-to-br from-[#4F46E5] to-[#7C3AED] rounded-xl text-white"
              >
                <div className="flex items-start justify-between mb-2">
                  <Award className="w-5 h-5" />
                  <span className="px-2 py-1 bg-white/20 rounded-full text-xs">
                    {scholarship.status}
                  </span>
                </div>
                <h4 className="text-white mb-2">{scholarship.name}</h4>
                <p className="text-2xl mb-2">${scholarship.amount.toFixed(2)}</p>
                <p className="text-sm text-white/80">{scholarship.period}</p>
              </div>
            ))}

            <div className="p-4 bg-[#F5F7FA] rounded-xl border-2 border-dashed border-[#E5E7EB]">
              <p className="text-gray-600 text-center">Apply for Additional Aid</p>
              <button className="w-full mt-3 px-4 py-2 bg-white border border-[#E5E7EB] text-gray-700 rounded-lg hover:bg-gray-50 transition-colors">
                View Opportunities
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
