import { RiRobot3Line } from "@remixicon/react";

const feature = {
  icon: <RiRobot3Line className="text-4x" />,
};

export default function ChatHeader() {
  return (
    <div className="flex items-center gap-3 px-6 py-4 border-b border-white/10">
      <div className="w-10 h-10 rounded-full bg-purple-600 flex items-center justify-center text-white font-bold">
        <span className="text-white text-xs">{feature.icon}</span>
      </div>
      <div>
        <p className="text-white font-semibold">MooVy bot</p>
        <p className="text-green-400 text-xs">En ligne</p>
      </div>
    </div>
  );
}
