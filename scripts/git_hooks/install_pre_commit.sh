#!/bin/sh

pre_commit_file="$(git rev-parse --show-toplevel)/.git/hooks/pre-commit"

if [ -f "${pre_commit_file}" ]
then
	echo "FILE ALREADY EXISTS!"
else
	echo '#!/bin/sh' >> "${pre_commit_file}" && echo "pytest" >> "${pre_commit_file}"&&echo "flake8 --exclude='ipython_log.py*,migrations,templates, manage.py' ." >> "${pre_commit_file}"
	chmod +x "${pre_commit_file}"
	echo "If you want to disable verifications (at risk), edit ${pre_commit_file}."
fi