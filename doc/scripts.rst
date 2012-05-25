Scripts
=======

Command-line scripts for use with born-digital archival materials. 

export-email
------------

**export-email** is a command-line script for exporting email content
from binary, proprietary folder formats into individual email messages
and attachment files, to allow individual email messages to be
scrutinized and archived.

Currently, the only supported email format is Outlook Express 4.5 for
Macintosh, but we expect to add support for other formats as we
encounter them.

Example usage::

  $ export-emails -d "Internet Mail" -o email-output

Where ``Internet Mail`` is the directory that contains Outlook Express
folders such as Inbox, Outbox, and Sent Mail, and ``email-output`` is
a folder where the exported messages should be saved. On our hardware,
the Outlook Express directory structure looks like this::

  Internet
  +- Internet Applications
     +- Outlook Express 4.5 Folder
        +- OE User(s)
           +- Account Name 1
           |  +- Internet Mail
           |     +- Deleted Messages
           |     +- Drafts
           |     +- Inbox
           |     +- Outbox
           |     +- Sent Mail
           +- Account Name 2
           |  +- Internet Mail
           |     +- Deleted Messages
           |     +- Drafts
           |     +- Inbox
           |     +- Outbox
           |     +- Sent Mail

If you with to export email messages for multiple accounts, you will
need to run ``export-email`` once for each account, giving it the
appropriate ``Internet Mail`` folder name.


output
^^^^^^

As it runs, ``export-email`` will report on the Mail folders it
identifies, the number of messages expected and the number of messages
and attachments exported.  

The script generates individual text files for email messages in each
folder.  The generated filenames include the folder name, message
date, who the message was from (or who the message was sent to for the
Sent Mail folder), and the subject.  If an email message includes
attachments with a filename, ``export-email`` will create a file in a
``_parts`` directory matching the output file name for the email
message.

In some cases, the folder index references deleted messages; these are
currently skipped for output, but a count of skipped deleted messages
will be reported when the script is run.  In other cases, there are
content sections in the folder data file which are not referenced by
the folder index (i.e., when the index and data files are apparently
not synchronized); these cannot exported, but a summary of the number
of skipped sections is included in the script output in case further
investigation is needed.

.. Note::

   Requires Python2.7 (due to use of :mod:`argparse`).






