// Open Build website forms → admin@open-build.org.
// Lives in Apps Script as "Open Build website forms" (admin@open-build.org), deployed as a web app (runs as admin@, anyone can post).
// site.js posts each form here. Every submission is emailed to admin@ with the sender as reply-to. The script can only send mail (MailApp,
// "Send email as you"), not read it: Gmail filters in admin@ file "Society lead:" mail under leads-societies and "Sponsor lead:" under leads-sponsors.
// After editing: paste into the Apps Script project, then Deploy > Manage deployments > edit > New version, so the /exec URL stays the same.

const TO = 'admin@open-build.org';

const FORMS = {
  society: {
    subject: d => `Society lead: ${d.society} (${d.uni})`,
    fields: [['Society', 'society'], ['Uni', 'uni'], ['Society email', 'email'], ["What they're after", 'need'], ["Next year's contact", 'handover']],
  },
  partner: {
    subject: d => `Sponsor lead: ${d.org} (${d.name})`,
    fields: [['Name', 'name'], ['Work email', 'email'], ['Organisation', 'org'], ["They'd like to", 'want'], ['Anything else', 'notes']],
  },
  news: {
    subject: d => `Event news sign-up: ${d.email}`,
    fields: [['Email', 'email']],
  },
};

function doPost(e) {
  const d = e.parameter;
  const form = FORMS[d.form];
  // Unknown form, or the hidden "website" field was filled in (a bot): drop it quietly
  if (!form || d.website) return reply('ok');
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email || '')) return reply('bad email');

  const clip = (s, n = 2000) => String(s || '').trim().slice(0, n);
  const body = form.fields.map(([name, key]) => `${name}: ${clip(d[key]) || '-'}`).join('\n')
    + `\n\nSent from the form on open-build.org${clip(d.page, 100)}. Reply to this email to answer them.`;
  MailApp.sendEmail(TO, clip(form.subject(d), 200), body, { replyTo: d.email, name: 'Open Build website' });
  return reply('ok');
}

function reply(text) {
  return ContentService.createTextOutput(text);
}
