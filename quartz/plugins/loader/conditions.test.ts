import test from "node:test"
import assert from "node:assert/strict"
import { getCondition } from "./conditions"
import type { QuartzComponentProps } from "../../components/types"

const noH1 = getCondition("no-h1")!

function propsWithTree(tree: unknown): QuartzComponentProps {
  return { tree } as QuartzComponentProps
}

test("automatic article title appears only when the Markdown has no H1", () => {
  assert.equal(noH1(propsWithTree({ type: "root", children: [] })), true)
  assert.equal(
    noH1(
      propsWithTree({
        type: "root",
        children: [
          { type: "element", tagName: "h2", properties: {}, children: [] },
        ],
      }),
    ),
    true,
  )
  assert.equal(
    noH1(
      propsWithTree({
        type: "root",
        children: [
          {
            type: "element",
            tagName: "section",
            properties: {},
            children: [
              { type: "element", tagName: "h1", properties: {}, children: [] },
            ],
          },
        ],
      }),
    ),
    false,
  )
})
