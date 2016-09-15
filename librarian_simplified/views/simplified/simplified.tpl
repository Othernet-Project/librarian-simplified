<%inherit file="/narrow_base.tpl"/>
<%namespace name="simplified_form" file="_simplified.tpl"/>

<%block name="title">
## Translators, used as page title
${_('Home Content Editor')}
</%block>

<h2>${_('Home Content Editor')}</h2>

${simplified_form.body()}