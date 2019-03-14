import ReactDOM from 'react-dom';
import React from 'react';
import { withStyles } from '@material-ui/core/styles';

import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

const styles = theme => ({
});

class MessageBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open: true,
    }
  }

  componentWillMount() {
  }

  componentWillUnmount() {
  }

  failIt() {
    ReactDOM.render(
      <img />,
      document.getElementById('modal'),
    );
  }

  handleOK() {
    this.failIt();
    if (this.props.callbackOK) {
      this.props.callbackOK();
    }
  }

  handleCancel() {
    this.failIt();
    if (this.props.callbackCancel) {
      this.props.callbackCancel();
    }
  }

  showDialog() {
    const {classes} = this.props;
    const result = () => (
      <div key={this.props.title}>
        <div>
          <Dialog
            open={this.state.open}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
          >
            <DialogTitle id="alert-dialog-title">
              {this.props.title}
            </DialogTitle>
            <DialogContent>
              <DialogContentText id="alert-dialog-description">
                {this.props.message}
              </DialogContentText>
            </DialogContent>
            <DialogActions>
              <Button onClick={(e)=>{this.handleCancel()}} color="primary">
                Cancel
              </Button>
              <Button onClick={(e)=>{this.handleOK()}} color="primary" autoFocus>
                OK
              </Button>
            </DialogActions>
          </Dialog>
        </div>
      </div>
    )
    return result();
  }

  render() {
    return (
      <div>
        {this.showDialog()}
      </div>
    );
  }
}

export default withStyles(styles)(MessageBox);
