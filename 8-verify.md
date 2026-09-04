1. Run `/code-review` to walk the changes and flag issues.
2. Look close at the output from `git diff`



Making sure that Claude actually runs the tests instead of trusting its claim:
- Create a  `stop hook` that runs your tests and refuses to rend the turn on a failure.
- Create a `post-tool-use hook` that lints and type checks after every edit.

The key detail is the exist code. A hook that exits with `exit 2` feeds the failure straight back into Claude without you asking and Claude reads the failure and fixes accordingly. 

- Get a cold second opinion on anything that matters.