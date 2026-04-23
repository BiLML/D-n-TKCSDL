import { User, Mail, Phone, MapPin, Lock, Shield, Bell, Moon } from 'lucide-react';
import { useState } from 'react';

export function Settings() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [emailNotifications, setEmailNotifications] = useState(true);
  const [pushNotifications, setPushNotifications] = useState(true);

  return (
    <div className="grid grid-cols-2 gap-6">
      <div className="col-span-2">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h3 className="mb-6">Personal Information</h3>
          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="block text-gray-600 mb-2">Full Name</label>
              <div className="flex items-center gap-3 px-4 py-3 bg-[#F5F7FA] border border-[#E5E7EB] rounded-lg">
                <User className="w-5 h-5 text-gray-400" />
                <input
                  type="text"
                  value="Alex Johnson"
                  className="flex-1 bg-transparent focus:outline-none"
                  readOnly
                />
              </div>
            </div>

            <div>
              <label className="block text-gray-600 mb-2">Student ID</label>
              <div className="flex items-center gap-3 px-4 py-3 bg-[#F5F7FA] border border-[#E5E7EB] rounded-lg">
                <input
                  type="text"
                  value="ST2024-8956"
                  className="flex-1 bg-transparent focus:outline-none"
                  readOnly
                />
              </div>
            </div>

            <div>
              <label className="block text-gray-600 mb-2">Email Address</label>
              <div className="flex items-center gap-3 px-4 py-3 bg-[#F5F7FA] border border-[#E5E7EB] rounded-lg">
                <Mail className="w-5 h-5 text-gray-400" />
                <input
                  type="email"
                  value="alex.johnson@university.edu"
                  className="flex-1 bg-transparent focus:outline-none"
                />
              </div>
            </div>

            <div>
              <label className="block text-gray-600 mb-2">Phone Number</label>
              <div className="flex items-center gap-3 px-4 py-3 bg-[#F5F7FA] border border-[#E5E7EB] rounded-lg">
                <Phone className="w-5 h-5 text-gray-400" />
                <input
                  type="tel"
                  value="+1 (555) 123-4567"
                  className="flex-1 bg-transparent focus:outline-none"
                />
              </div>
            </div>

            <div className="col-span-2">
              <label className="block text-gray-600 mb-2">Address</label>
              <div className="flex items-center gap-3 px-4 py-3 bg-[#F5F7FA] border border-[#E5E7EB] rounded-lg">
                <MapPin className="w-5 h-5 text-gray-400" />
                <input
                  type="text"
                  value="456 Campus Drive, University City, ST 12345"
                  className="flex-1 bg-transparent focus:outline-none"
                />
              </div>
            </div>
          </div>

          <div className="mt-6 flex justify-end">
            <button className="px-6 py-2 bg-[#4F46E5] text-white rounded-lg hover:bg-[#4338CA] transition-colors">
              Save Changes
            </button>
          </div>
        </div>
      </div>

      <div className="col-span-1">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h4 className="mb-6">Security</h4>
          <div className="space-y-4">
            <button className="w-full flex items-center justify-between px-4 py-4 bg-[#F5F7FA] hover:bg-gray-100 rounded-lg transition-colors">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-[#4F46E5]/10 rounded-lg flex items-center justify-center">
                  <Lock className="w-5 h-5 text-[#4F46E5]" />
                </div>
                <div className="text-left">
                  <p className="text-gray-900">Change Password</p>
                  <p className="text-gray-500">Last changed 3 months ago</p>
                </div>
              </div>
              <svg
                className="w-5 h-5 text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>

            <button className="w-full flex items-center justify-between px-4 py-4 bg-[#F5F7FA] hover:bg-gray-100 rounded-lg transition-colors">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-[#4F46E5]/10 rounded-lg flex items-center justify-center">
                  <Shield className="w-5 h-5 text-[#4F46E5]" />
                </div>
                <div className="text-left">
                  <p className="text-gray-900">Two-Factor Authentication</p>
                  <p className="text-green-600">Enabled</p>
                </div>
              </div>
              <svg
                className="w-5 h-5 text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div className="col-span-1">
        <div className="bg-white rounded-2xl border border-[#E5E7EB] p-6 shadow-sm">
          <h4 className="mb-6">Preferences</h4>
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-[#4F46E5]/10 rounded-lg flex items-center justify-center">
                  <Moon className="w-5 h-5 text-[#4F46E5]" />
                </div>
                <div>
                  <p className="text-gray-900">Dark Mode</p>
                  <p className="text-gray-500">Toggle dark theme</p>
                </div>
              </div>
              <button
                onClick={() => setIsDarkMode(!isDarkMode)}
                className={`relative w-12 h-6 rounded-full transition-colors ${
                  isDarkMode ? 'bg-[#4F46E5]' : 'bg-gray-300'
                }`}
              >
                <span
                  className={`absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform ${
                    isDarkMode ? 'translate-x-6' : 'translate-x-0'
                  }`}
                ></span>
              </button>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-[#4F46E5]/10 rounded-lg flex items-center justify-center">
                  <Bell className="w-5 h-5 text-[#4F46E5]" />
                </div>
                <div>
                  <p className="text-gray-900">Email Notifications</p>
                  <p className="text-gray-500">Receive updates via email</p>
                </div>
              </div>
              <button
                onClick={() => setEmailNotifications(!emailNotifications)}
                className={`relative w-12 h-6 rounded-full transition-colors ${
                  emailNotifications ? 'bg-[#4F46E5]' : 'bg-gray-300'
                }`}
              >
                <span
                  className={`absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform ${
                    emailNotifications ? 'translate-x-6' : 'translate-x-0'
                  }`}
                ></span>
              </button>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-[#4F46E5]/10 rounded-lg flex items-center justify-center">
                  <Bell className="w-5 h-5 text-[#4F46E5]" />
                </div>
                <div>
                  <p className="text-gray-900">Push Notifications</p>
                  <p className="text-gray-500">Get notified instantly</p>
                </div>
              </div>
              <button
                onClick={() => setPushNotifications(!pushNotifications)}
                className={`relative w-12 h-6 rounded-full transition-colors ${
                  pushNotifications ? 'bg-[#4F46E5]' : 'bg-gray-300'
                }`}
              >
                <span
                  className={`absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full transition-transform ${
                    pushNotifications ? 'translate-x-6' : 'translate-x-0'
                  }`}
                ></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
