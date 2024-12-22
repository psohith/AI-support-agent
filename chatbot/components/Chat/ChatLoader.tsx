import { FC } from "react";

interface Props {}

export const ChatLoader: FC<Props> = () => {
  return (
    <div className="flex flex-row items-center">
      <div className="flex-shrink-0 w-8">
        <img
          src="/testsigma_logo.jpeg"
          alt="Bot"
          className="w-8 h-8 rounded-full"
        />
      </div>
      <div
        className="flex items-center bg-neutral-200 text-neutral-900 rounded-2xl px-4 py-2 w-fit ms-4"
        style={{ overflowWrap: "anywhere" }}
      >
        <div className="flex space-x-1 p-2">
          <span className="w-2 h-2 bg-neutral-800 rounded-full animate-bounce"></span>
          <span className="w-2 h-2 bg-neutral-800 rounded-full animate-bounce [animation-delay:0.2s]"></span>
          <span className="w-2 h-2 bg-neutral-800 rounded-full animate-bounce [animation-delay:0.4s]"></span>
        </div>
      </div>
    </div>
  );
};
