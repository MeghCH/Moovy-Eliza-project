import { RiSearchLine } from "@remixicon/react";

type SearchBarProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function SearchBar({ value, onChange }: SearchBarProps) {
  return (
    <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-full px-5 py-3 mb-8 focus-within:border-purple-500 transition-colors">
      <RiSearchLine className="text-gray-400 shrink-0" size={18} />
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Rechercher une conversation..."
        className="bg-transparent text-white text-sm outline-none w-full placeholder-gray-500"
      />
    </div>
  );
}
