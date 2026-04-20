ifneq ($(suffix $(spec)),.spec)
	override spec := $(spec)/libfprint-2-tod1-elan-0c4b.spec
endif

srpm:
	dnf -y install spectool rpmautospec rpm-build
	spectool -g "$(spec)"
	rpmautospec process-distgit "$(spec)" "$(spec)"
	rpmbuild -bs "$(spec)" \
			--define "_sourcedir $(PWD)" \
			--define "_srcrpmdir $(outdir)" \
			--define "_topdir $(PWD)/rpmbuild"
