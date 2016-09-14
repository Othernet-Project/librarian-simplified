<%inherit file="/base.tpl"/>

<%block name="title">
## Translators, used as page title
${_('Files')}
</%block>

<%block name="extra_head">
<link rel="stylesheet" type="text/css" href="${assets['css/filemanager']}" />
</%block>

<%block name="main">
    <div class="o-main-inner" id="main-container">
        <div class="views-container-simple" id="views-container">
            <div class="views-main">
                % if 'html' not in current.meta.content_type_names:
                <span class="note">${_('No documents to be shown.')}</span>
                % else:
                <%
                    filename = (current.meta.get('main', language=request.locale) or
                                current.meta.get('main', language='__auto__'))
                    if path:
                        full_path = th.join(path, filename)
                    else:
                        full_path = filename
                %>
                <div class="views-reader" id="views-reader">
                    <iframe class="views-reader-frame" src="${h.quoted_url('filemanager:direct', path=full_path)}" id="views-reader-frame" data-content="${content}" data-placeholder="${placeholder}"></iframe>
                </div>
                % endif
            </div>
        </div>
    </div>
</%block>

<%block name="extra_scripts">
<script src="${assets['js/simplified']}"></script>
</%block>
