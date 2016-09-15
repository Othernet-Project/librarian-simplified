<%namespace name="forms" file="/ui/forms.tpl"/>

${forms.form_message(message) if message else ''}
${forms.form_errors([form.error]) if form.error else ''}

<form action="${i18n_url('simplified:editor')}" method="POST" id="simplified-form">
    ${forms.field(form.content)}
    <p class="buttons">
        <button type="submit">${_('Save')}</button>
    </p>
</form>
