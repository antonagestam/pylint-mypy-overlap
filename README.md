# pylint-mypy-overlap

Attempt to map the current overlap between [Pylint checks that are not yet 
implemented in ruff][pylint-ruff] and mypy.

The process was very manual. I went through each rule on the Pylint issue in
ruff that wasn't marked as implemented, looked up the rule in the Pylint
documentation and copied the example to a local file.

On each file I ran `mypy --strict` and manually determined whether mypy was
giving an equivalent error or not. Sometimes the example had to be modified
because mypy was giving errors for orthogonal or irrelevant issues.

Examples with a clear equivalent error were moved to `mypy-overlap/`,
and respectively, those without an equivalent error were moved to
`pylint-only/`.

I failed to reproduce a few examples and determined a few invalid or outdated,
those were moved to `deferred/` and `invalid/` respectively.

One rule was partially implemented in mypy, where pylint seemingly has it's
own definition of implicit abstract methods. This example can be found under
`partial-overlap/`.
