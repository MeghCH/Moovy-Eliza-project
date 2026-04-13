import { RiSendPlaneFill } from "@remixicon/react";

type ChatInputProps = {
  input: string;
  onChange: (value: string) => void;
  onSend: () => void;
};

export default function ChatInput({ input, onChange, onSend }: ChatInputProps) {
  return (
    <div className="px-6 py-4 border-t border-white/10 flex gap-3 items-center">
      <input
        type="text"
        value={input}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && onSend()}
        placeholder="Un film, une ambiance..."
        className="flex-1 bg-white/5 border border-white/10 rounded-full px-5 py-3 text-white text-sm placeholder-gray-500 outline-none focus:border-purple-500 transition-colors"
      />
      <button
        onClick={onSend}
        className="w-11 h-11 bg-purple-600 hover:bg-purple-700 rounded-full flex items-center justify-center transition-colors shrink-0"
      >
        <RiSendPlaneFill className="text-white text-lg" />
      </button>
    </div>
  );
}
