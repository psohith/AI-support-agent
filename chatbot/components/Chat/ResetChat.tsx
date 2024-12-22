import { FC } from "react";
import { IconTrash } from "@tabler/icons-react";

interface Props {
  onReset: () => void;
}

export const ResetChat: FC<Props> = ({ onReset }) => {
  return (
    <div className="flex flex-row items-center">
      <button
        className="text-neutral-900 rounded-lg p-2 mb-2 bg-neutral-200 hover:bg-neutral-300 focus:outline-none focus:ring-1 focus:ring-neutral-300 transition-colors"
        onClick={() => onReset()}
        title="Start New Chat"
      >
        <IconTrash size={24} />
      </button>
    </div>
  );
};
