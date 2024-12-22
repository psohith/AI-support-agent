import { Message } from "@/types";
import { FC } from "react";
import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { atomDark } from "react-syntax-highlighter/dist/cjs/styles/prism";
import remarkGfm from "remark-gfm";

interface Props {
  message: Message;
}

export const ChatMessage: FC<Props> = ({ message }) => {
  return (
    <div
      className={`flex flex-col ${
        message.role === "assistant" ? "items-start" : "items-end"
      } mb-6`}
    >
      <div className="flex items-start space-x-4 relative w-full">
        {message.role === "assistant" && (
          <div className="flex-shrink-0 w-8">
            <img
              src="/testsigma_logo.jpeg"
              alt="Bot"
              className="w-8 h-8 rounded-full"
            />
          </div>
        )}
        <div
          className={`flex items-center ${
            message.role === "assistant"
              ? "bg-neutral-200 text-black font-normal"
              : "bg-blue-500 text-white ml-auto mr-12"
          } rounded-2xl px-4 py-3 max-w-[67%]`}
        >
          {message.role === "assistant" ? (
            <div className="markdown-body w-full text-black">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                className="prose prose-sm prose-black max-w-none"
                components={{
                  code({ node, inline, className, children, ...props }) {
                    const match = /language-(\w+)/.exec(className || "");
                    return !inline && match ? (
                      <SyntaxHighlighter
                        language={match[1]}
                        style={atomDark}
                        PreTag="div"
                        className="rounded-md"
                        {...props}
                      >
                        {String(children).replace(/\n$/, "")}
                      </SyntaxHighlighter>
                    ) : (
                      <code
                        className={`${className} bg-gray-800 rounded-md px-1 py-0.5 text-sm`}
                        {...props}
                      >
                        {children}
                      </code>
                    );
                  },
                  p: ({ children }) => (
                    <p className="mb-4 last:mb-0 text-black">{children}</p>
                  ),
                  ul: ({ children }) => (
                    <ul className="list-disc list-inside space-y-2 mb-4 text-black">
                      {children}
                    </ul>
                  ),
                  ol: ({ children }) => (
                    <ol className="list-decimal space-y-2 mb-4 text-black">
                      {children}
                    </ol>
                  ),
                  li: ({ children }) => (
                    <li className="ml-4 text-black">{children}</li>
                  ),
                }}
              >
                {message.content}
              </ReactMarkdown>
            </div>
          ) : (
            <div
              className="whitespace-pre-wrap"
              style={{ overflowWrap: "anywhere" }}
            >
              {message.content}
            </div>
          )}
        </div>
        {message.role !== "assistant" && (
          <div className="flex-shrink-0 w-8 absolute right-0">
            <img
              src="/user_logo.png"
              alt="User"
              className="w-8 h-8 rounded-full"
            />
          </div>
        )}
      </div>
    </div>
  );
};
