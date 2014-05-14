from expects import expect

from mamba import formatters, reporter

from spec.object_mother import *


with description(formatters.XUnitFormatter):

    with before.all:
        self.example_group = an_example_group()
        self.example = an_example()
        self.example_group.append(self.example)

        self.formatter = formatters.XUnitFormatter()
        self.reporter = reporter.Reporter(self.formatter)

        self.reporter.start()
        self.example_group.run(self.reporter)
        self.reporter.finish()

        self.root = self.formatter.root

    with it('contains testsuites as root'):
        expect(self.root.tag).to.be('testsuites')

    with it('contains mamba as name for root'):
        expect(self.root.get('name')).to.be('mamba')

    with it('contains testsuite for example group'):
        expect(self.root.find('testsuite')).to.not_be.none

    with it('contains example group subject for testsuite'):
        expect(self.root.find('testsuite').get('name')).to.be(IRRELEVANT_SUBJECT)

    with it('contains testcase for example'):
        expect(self.root.find('testsuite').find('testcase')).to.not_be.none

    with it('contains example group subject for testcase'):
        expect(self.root.find('testsuite').find('testcase').get('name')).to.be(self.example.name)

