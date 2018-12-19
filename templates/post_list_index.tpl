## -*- coding: utf-8 -*-
<%block name="content">
<!-- Begin post-list ${post_list_id} -->
<div id="${post_list_id}" class="post-list">
    %if posts:
    <ul class="post-list">
        % for post in posts:
            <li class="post-list-item">
            <a href="${post.permalink(lang)}">${post.title(lang)|h}</a>
            </li>
        % endfor
    </ul>
    %endif
</div>
<!-- End post-list ${post_list_id} -->
</%block>
